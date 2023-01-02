<template>
  <div>
    <el-tooltip :content="$t('msg.navBar.guide')">
      <svg-icon
        id="guide-start"
        icon="guide"
        class="icon"
        @click="onClick"
      ></svg-icon>
    </el-tooltip>
  </div>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import Driver from 'driver.js'
import 'driver.js/dist/driver.min.css'
import { onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { steps } from './step'

const i18n = useI18n()
let driver = null

onMounted(() => {
  driver = new Driver({
    animate: true,
    opacity: 0.7,
    padding: 0,
    allowClose: false,
    closeBtnText: i18n.t('msg.guide.close'),
    doneBtnText: 'Done',
    nextBtnText: i18n.t('msg.guide.next'),
    prevBtnText: i18n.t('msg.guide.prev')
  })
})

function onClick() {
  driver.defineSteps(steps(i18n))
  driver.start()
}
</script>

<style scoped></style>
