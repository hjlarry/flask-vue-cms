import { useIntersectionObserver } from '@vueuse/core'

/*
图片懒加载，先把img标签的src设置为空，然后使用IntersectionObserver监听img标签是否进入可视区域，如果进入可视区域，再把img标签的src设置为真实的图片地址
*/
export default {
  mounted(el) {
    const imgSrc = el.src
    el.src = ''
    const { stop } = useIntersectionObserver(el, ([{ isIntersecting }]) => {
      if (isIntersecting) {
        el.src = imgSrc
        stop()
      }
    })
  }
}
