import { createI18n } from 'vue-i18n'
import { getItem } from '@/utils/storage'
import { LANG } from '@/constant'

const messages = {
  en: {
    msg: {
      hello: 'Hello world'
    }
  },
  cn: {
    msg: {
      hello: '你好，世界'
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

export default i18n
