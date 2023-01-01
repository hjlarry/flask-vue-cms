<template>
  <div class="pan-item" :style="{ width: width, height: height }">
    <div class="pan-info">
      <div class="pan-info-container">
        <slot />
      </div>
    </div>
    <div class="pan-thumb" :style="{ backgroundImage: `url(${image})` }"></div>
  </div>
</template>

<script setup>
defineProps({
  image: {
    type: String
  },
  width: {
    type: String,
    default: '150px'
  },
  height: {
    type: String,
    default: '150px'
  }
})
</script>

<style lang="scss" scoped>
.pan-item {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  display: inline-block;
  cursor: pointer;
  position: relative;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  .pan-thumb {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    position: absolute;
    transform-origin: 95% 40%;
    transition: all 0.5s ease-in-out;
  }
  .pan-info {
    width: inherit;
    height: inherit;
    border-radius: 50%;
    position: absolute;
    box-shadow: inset 0 0 0 5px rgba(0, 0, 0, 0.05);
    .pan-info-container {
      text-align: center;
      display: block;
      color: #333;
      width: 80px;
      height: 80px;
      background: rgba(255, 255, 255, 0.5);
      border-radius: 50%;
      font-style: normal;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 9px;
      letter-spacing: 1px;
      padding-top: 24px;
      margin: 7px auto 0;
      font-family: 'Open Sans', Arial, sans-serif;
      opacity: 0;
      transition: transform 0.3s ease-in-out 0.2s, opacity 0.3s ease-in-out 0.2s,
        background 0.2s linear 0s;
      transform: translateX(60px) rotate(90deg);
    }
  }
  &:hover .pan-thumb {
    transform: rotate(-110deg);
  }
  &:hover .pan-info-container {
    opacity: 1;
    transform: translateX(0px) rotate(0deg);
  }
}
</style>
