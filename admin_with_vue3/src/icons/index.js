import SvgIcon from '@/components/SvgIcon/index.vue' // svg component

const svgRequire = import.meta.globEager('@/icons/svg/**/*.svg')
console.log(svgRequire)
// svgRequire.keys().forEach((svgIcon) => svgRequire(svgIcon))

export default (app) => {
  app.component('svg-icon', SvgIcon)
}
