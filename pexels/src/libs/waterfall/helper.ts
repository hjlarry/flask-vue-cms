export const getMinHeight = (columnHeightObj) => {
  const columnHeightArr = Object.values(columnHeightObj)
  return Math.min(...columnHeightArr)
}

export const getMaxHeight = (columnHeightObj) => {
  const columnHeightArr = Object.values(columnHeightObj)
  return Math.max(...columnHeightArr)
}

export const getMinHeightColumn = (columnHeightArr): number => {
  const minHeight = Math.min(...columnHeightArr)
  return columnHeightArr.findIndex((item) => item === minHeight)
}

export const waitImgLoaded = (imgs) => {
  const promiseArr = []
  imgs.forEach((img, index) => {
    promiseArr[index] = new Promise((resolve, reject) => {
      const imgObj = new Image()
      imgObj.src = img
      imgObj.onload = () => {
        resolve({ img, index })
      }
    })
  })
  return Promise.all(promiseArr)
}
