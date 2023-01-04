import dayjs from 'dayjs'

function dateFilter(value, format = 'DD.MM.YYYY') {
  return dayjs(value).format(format)
}

export default function (app) {
  app.config.globalProperties.$filters = {
    dateFilter
  }
}
