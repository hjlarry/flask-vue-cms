import lazy from './modules/lazy'

export default (app) => {
  app.directive('lazy', lazy)
}
