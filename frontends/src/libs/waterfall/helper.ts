export const getMinHeight = (columnHeightObj) => {
  const columnHeightArr = Object.values(columnHeightObj)
  // console.log(columnHeightObj, 122121)
  // console.log(columnHeightArr, 1221)
  return Math.min(...columnHeightArr)
}

export const getMaxHeight = (columnHeightObj) => {
  const columnHeightArr = Object.values(columnHeightObj)
  return Math.max(...columnHeightArr)
}

export const getMinHeightColumn = (columnHeightObj): number => {
  const minHeight = getMinHeight(columnHeightObj)
  // console.log(minHeight, 12312)
  return Object.keys(columnHeightObj).find(
    (key) => columnHeightObj[key] === minHeight
  )
}
