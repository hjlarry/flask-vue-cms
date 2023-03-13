import dayjs from 'dayjs'
import rt from 'dayjs/plugin/relativeTime'

dayjs.extend(rt)

function dateFilter(value, format = 'DD.MM.YYYY') {
  return dayjs(value).format(format)
}

function relativeTime(value) {
  if (value) {
    return dayjs().to(dayjs(value))
  }
}

export default function (app) {
  app.config.globalProperties.$filters = {
    dateFilter,
    relativeTime
  }
}
