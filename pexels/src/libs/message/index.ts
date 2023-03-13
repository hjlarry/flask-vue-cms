import { h, render } from 'vue'
import messageComponent from './index.vue'

export const message = (
  type: string,
  content: string,
  duration: number = 3000
) => {
  const onDestroy = () => {
    render(null, document.body)
  }

  const vnode = h(messageComponent, {
    type,
    content,
    duration,
    onClose: onDestroy
  })
  render(vnode, document.body)
}
