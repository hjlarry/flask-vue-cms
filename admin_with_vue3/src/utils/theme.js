import axios from 'axios'
import color from 'css-color-function'
import rgbHex from 'rgb-hex'
import formula from '@/constant/formula.json'

async function getOriginStyle() {
  const version = require('element-plus/package.json').version
  const url = `https://unpkg.com/element-plus@${version}/dist/index.css`
  let { data } = await axios.get(url)
  const colorMap = {
    '#3a8ee6': 'shade-1',
    '#0d84ff': 'shade-1',
    '#409eff': 'primary',
    '#53a8ff': 'light-1',
    '#66b1ff': 'light-2',
    '#79bbff': 'light-3',
    '#8cc5ff': 'light-4',
    '#a0cfff': 'light-5',
    '#b3d8ff': 'light-6',
    '#c6e2ff': 'light-7',
    '#d9ecff': 'light-8',
    '#ecf5ff': 'light-9',
    // 避免找字体404
    'src:url\\(fonts/element-icons.woff\\)': ''
  }
  Object.keys(colorMap).forEach((key) => {
    const value = colorMap[key]
    data = data.replace(new RegExp(key, 'ig'), value)
  })
  console.log(data)
  return data
}

export function genNewColor(primary) {
  if (!primary) return
  const colors = { primary }
  Object.keys(formula).forEach((key) => {
    const value = formula[key].replace(/primary/g, primary)
    colors[key] = '#' + rgbHex(color.convert(value))
  })
  return colors
}

export async function genNewStyle(primaryColor) {
  let cssText = await getOriginStyle()
  const colors = genNewColor(primaryColor)
  Object.keys(colors).forEach((key) => {
    cssText = cssText.replace(
      new RegExp('(:|\\s+)' + key, 'g'),
      '$1' + colors[key]
    )
  })
  return cssText
}

export function writeNewStyle(cssText) {
  const style = document.createElement('style')
  style.innerText = cssText
  document.head.appendChild(style)
}
