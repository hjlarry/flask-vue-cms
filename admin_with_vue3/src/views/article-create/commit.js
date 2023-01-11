import { createArticle, editArticle } from '@/api/article'
import { ElMessage } from 'element-plus'
import i18n from '@/i18n'

export async function articleCreate(data) {
  const res = await createArticle(data)
  ElMessage.success(i18n.global.t('msg.article.createSuccess'))
  return res
}

export async function articleEdit(id, data) {
  const res = await editArticle(id, data)
  ElMessage.success(i18n.global.t('msg.article.editSuccess'))
  return res
}
