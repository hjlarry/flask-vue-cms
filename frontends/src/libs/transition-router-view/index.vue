<template>
  <RouterView v-slot="{ Component }">
    <Transition :name="transitionName">
      <component :is="Component" />
    </Transition>
  </RouterView>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps<{
  routerType: 'push' | 'back' | 'none'
}>()

const transitionName = ref('')
const router = useRouter()
router.beforeEach((to, form) => {
  transitionName.value = props.routerType
})
</script>

<style scoped>
/* push时，新页面进入动画 */
.push-enter-active {
  animation-name: push-in;
  animation-duration: 0.5s;
}
/* push时，老页面退出动画 */
.push-leave-active {
  animation-name: push-out;
  animation-duration: 0.5s;
}

@keyframes push-in {
  0% {
    transform: translate(100%, 0);
  }
  100% {
    transform: translate(0, 0);
  }
}

@keyframes push-out {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(-50%, 0);
  }
}

/* 后退的页面进入动画 */
.back-enter-active {
  animation-name: back-in;
  animation-duration: 0.5s;
}
/* 老页面退出动画 */
.back-leave-active {
  animation-name: back-out;
  animation-duration: 0.5s;
}

@keyframes back-in {
  0% {
    transform: translate(-100%, 0);
  }
  100% {
    transform: translate(0, 0);
  }
}

@keyframes back-out {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(50%, 0);
  }
}
</style>
