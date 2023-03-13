<template>
  <div>
    <el-container>
      <el-main>
        <el-row>
          <el-col :span="6">
            <ProjectCard class="user-container" :features="featureData" />
          </el-col>
          <el-col :span="18">
            <el-card>
              <el-tabs v-model="activeName">
                <el-tab-pane :label="$t('msg.profile.feature')" name="feature">
                  <Feature :features="featureData"></Feature>
                </el-tab-pane>
                <el-tab-pane
                  :label="$t('msg.profile.timeline')"
                  name="timeline"
                >
                  <Timeline></Timeline>
                </el-tab-pane>
                <el-tab-pane :label="$t('msg.profile.about')" name="about">
                  <About></About>
                </el-tab-pane>
              </el-tabs>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import ProjectCard from './components/ProjectCard.vue'
import About from './components/About.vue'
import Feature from './components/Feature.vue'
import Timeline from './components/Timeline.vue'
import { ref } from 'vue'
import { getFeature } from '@/api/user'
import { watchSwitchLang } from '@/i18n'

const activeName = ref('feature')
const featureData = ref([])

const getFeatureData = async () => {
  const res = await getFeature()
  featureData.value = res.data
}
getFeatureData()
watchSwitchLang(getFeatureData)
</script>

<style lang="scss" scoped>
.user-container {
  margin-right: 20px;
}
</style>
