<template>
  <div>
    <div class=''>
      {{ $t('msg.route.profile') }}
    </div>
    <el-pagination
      v-model:current-page='currentPage1'
      :page-size='100'
      layout='total, prev, pager, next'
      :total='1000'
    />
    <el-row>
      <el-button>Default</el-button>
      <el-button type='primary'>Primary</el-button>
      <el-button type='success'>Success</el-button>
      <el-button type='info'>Info</el-button>
      <el-button type='warning'>Warning</el-button>
      <el-button type='danger'>Danger</el-button>
    </el-row>

    <el-scrollbar>
      <div class='scrollbar-flex-content'>
        <p v-for='item in 50' :key='item' class='scrollbar-demo-item'>
          {{ item }}
        </p>
      </div>
    </el-scrollbar>

    <el-dropdown trigger='click'>

      <span>
        <el-tooltip :content='$t("msg.navBar.lang")'>
        Dropdown List
        </el-tooltip>
      </span>

      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>Action 1</el-dropdown-item>
          <el-dropdown-item>Action 2</el-dropdown-item>
          <el-dropdown-item>Action 3</el-dropdown-item>
          <el-dropdown-item disabled>Action 4</el-dropdown-item>
          <el-dropdown-item divided>Action 5</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const currentPage1 = ref(5)
</script>

<style lang='scss' scoped>
.scrollbar-flex-content {
  display: flex;
}

.scrollbar-demo-item {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}

</style>
