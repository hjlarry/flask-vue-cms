import { createI18n } from 'vue-i18n'
import { watch } from 'vue'
import { getItem } from '@/utils/storage'
import { LANG } from '@/constant'

import myCn from './lang/zh'
import myEn from './lang/en'
import { appStore } from '@/store/app_store'

const messages = {
  en: {
    msg: {
      ...myEn
    }
  },
  cn: {
    msg: {
      ...myCn
    }
  }
}

const locale = getItem(LANG) || 'cn'

const i18n = createI18n({
  // 使用 Composition API 模式
  legacy: false,
  // 全局注入 $t 函数
  globalInjection: true,
  locale,
  messages
})

export function generateRouteTitle(title) {
  return i18n.global.t('msg.route.' + title)
}

export function watchSwitchLang(...cbs) {
  const aStore = appStore()
  watch(
    () => aStore.language,
    () => {
      cbs.forEach((cb) => cb(aStore.lang))
    }
  )
}

export default i18n
