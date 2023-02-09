<template>
  <div
    class="group rounded-xl relative p-0.5 border-white hover:bg-red-100/40 duration-500"
  >
    <m-svg-icon
      class="h-1.5 w-1.5 absolute left-2 top-[50%] translate-y-[-50%]"
      color="#707070"
      name="search"
    ></m-svg-icon>
    <input
      class="block duration-500 w-full h-[44px] pl-4 rounded-xl outline-0 text-sm font-semibold text-zinc-900 tracking-wide caret-zinc-400 border border-zinc-100 group-hover:border-zinc-200 focus:border-red-300 bg-zinc-100 group-hover:bg-white"
      placeholder="搜索"
    />
    <m-svg-icon
      class="h-1.5 w-1.5 absolute right-9 top-[50%] translate-y-[-50%] cursor-pointer duration-500"
      color="#707070"
      name="input-delete"
    ></m-svg-icon>
    <div
      class="h-1.5 w-[1px] absolute right-[62px] bg-zinc-200 top-[50%] translate-y-[-50%] opacity-0 group-hover:opacity-100 duration-500"
    ></div>

    <Transition name="slide">
      <div
        class="absolute duration-200 w-[96%] z-20 left-0 top-[56px] max-h-[368px] ml-1 p-2 overflow-auto bg-white text-base border border-zinc-200 rounded hover:shadow-2xl"
      >
        <slot name="dropdown" />
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.slide-enter-active {
  transition: all 0.5s;
}

.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateY(40px);
  opacity: 0;
}
</style>
