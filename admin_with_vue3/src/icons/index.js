import SvgIcon from '@/components/SvgIcon' // svg component

const svgRequire = require.context('./svg', false, /\.svg$/)

svgRequire.keys().forEach((svgIcon) => svgRequire(svgIcon))

export default (app) => {
  app.component('svg-icon', SvgIcon)
}
