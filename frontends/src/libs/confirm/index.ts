import { h, render } from 'vue'
import confirmComponent from './index.vue'

export const confirm = (
  title?: string,
  content?: string,
  cancelText: string = '取消',
  okText: string = '确定'
): Promise => {
  const p = new Promise((resolve, reject) => {
    // 支持title和content只传一个
    if (title && !content) {
      content = title
      title = ''
    }

    const okHandler = resolve
    const cancelHandler = () => {
      reject(new Error('click cancel button'))
    }
    const closeHandler = () => {
      render(null, document.body)
    }

    const vnode = h(confirmComponent, {
      title,
      content,
      cancelText,
      okText,
      okHandler,
      cancelHandler,
      closeHandler
    })
    render(vnode, document.body)
  })
  return p
}
