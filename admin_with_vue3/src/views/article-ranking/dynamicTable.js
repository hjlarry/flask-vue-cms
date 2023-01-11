import { ref, watch } from 'vue'
import i18n, { watchSwitchLang } from '@/i18n'

const t = i18n.global.t

function getDynamicData() {
  return [
    {
      label: t('msg.article.title'),
      prop: 'title'
    },
    {
      label: t('msg.article.author'),
      prop: 'author'
    },
    {
      label: t('msg.article.publicDate'),
      prop: 'publicDate'
    },
    {
      label: t('msg.article.desc'),
      prop: 'desc'
    },
    {
      label: t('msg.article.action'),
      prop: 'action'
    }
  ]
}
export const dynamicData = ref(getDynamicData())

export const selectedDynamicLabel = ref(
  getDynamicData().map((item) => item.label)
)

watchSwitchLang(() => {
  dynamicData.value = getDynamicData()
  selectedDynamicLabel.value = getDynamicData().map((item) => item.label)
})

export const tableColumns = ref([])

watch(
  selectedDynamicLabel,
  (val) => {
    tableColumns.value = []
    const selectData = dynamicData.value.filter((item) => {
      return val.includes(item.label)
    })
    tableColumns.value.push(...selectData)
  },
  {
    immediate: true
  }
)
