import { resultSuccess } from './_util'

const data = [
  {
    id: 0,
    title: '连续包月',
    desc: '次月 ¥19 续费,可随时取消',
    oldPrice: '29',
    price: '9',
    isHot: true
  },
  {
    id: 1,
    title: '连续包年',
    desc: '次月 ¥198 续费,可随时取消',
    oldPrice: '258',
    price: '198',
    isHot: false
  },
  {
    id: 2,
    title: '连续包季',
    desc: '次月 ¥53 续费,可随时取消',
    oldPrice: '68',
    price: '53',
    isHot: false
  },
  { id: 3, title: '月卡', desc: '', oldPrice: '39', price: '29', isHot: false },
  { id: 4, title: '季卡', desc: '', oldPrice: '79', price: '68', isHot: false },
  {
    id: 5,
    title: '年卡',
    desc: '',
    oldPrice: '298',
    price: '258',
    isHot: false
  }
]

export default [
  {
    url: '/mock/getVipPayList',
    method: 'GET',
    response: () => {
      return resultSuccess(data)
    }
  }
]
