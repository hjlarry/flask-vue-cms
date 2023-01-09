import { userStore } from '@/store/user_store'

function checkPermission(el, binding) {
  //   获取绑定的权限
  const { value } = binding

  const uStore = userStore()
  const points = uStore.userInfo.permissions.points

  if (value && value instanceof Array) {
    const hasPermission = points.some((point) => {
      return value.includes(point)
    })
    // 没有权限的，移除元素 不可见
    if (!hasPermission) {
      el.parentNode && el.parentNode.removeChild(el)
    }
  } else {
    throw new Error("v-permission value is ['something']")
  }
}

export default {
  // 在绑定元素的父组件被挂载后调用
  mounted(el, binding) {
    checkPermission(el, binding)
  },
  // 在包含组件的VNode及其子组件的VNode更新后调用
  update(el, binding) {
    checkPermission(el, binding)
  }
}
