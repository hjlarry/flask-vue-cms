<template>
  <div class='header-search' :class='{show:isShow}'>
    <svg-icon icon='search' class='search-icon' @click='toggleShowSearch'></svg-icon>
    <el-select
      filterable
      remote
      default-first-option
      placeholder='Search'
      ref='searchInputRef'
      class='header-search-input'
      v-model='searchWords'
      :remote-method='onSearch'
      @change='onSelectChange'
    >
      <el-option
        v-for='item in 5'
        :key='item'
        :label='item'
        :value='item'>
      </el-option>
    </el-select>
  </div>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import { ref } from 'vue'

const isShow = ref(false)
const searchWords = ref('')
const searchInputRef = ref(null)

function toggleShowSearch() {
  isShow.value = !isShow.value
  if (isShow.value) {
    searchInputRef.value.focus()
  }
}

function onSearch() {
  console.log(searchWords.value)
}

// 选中回调
function onSelectChange() {
  console.log(searchWords.value)
}
</script>

<style lang='scss' scoped>
.header-search {
  .search-icon {
    vertical-align: middle;
    margin-right: 10px;
  }

  .header-search-input {
    transition: width 0.2s;
    margin-right: 10px;
    width: 0;
    overflow: hidden;
    vertical-align: middle;

    :deep(.el-input__inner) {
      border: 0;
      border-radius: 0;
      border-bottom: 1px solid #e2e2e2;
    }
  }

  &.show {
    .header-search-input {
      width: 200px;
    }
  }
}
</style>
