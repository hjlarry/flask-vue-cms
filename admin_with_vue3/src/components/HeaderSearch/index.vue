<template>
  <div class='header-search' :class='{show:isShow}'>
    <svg-icon icon='search' class='search-icon' @click.stop='toggleShowSearch'></svg-icon>
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
        v-for='option in searchResults'
        :key='option.item.path'
        :label='option.item.title.join(">")'
        :value='option.item'>
      </el-option>
    </el-select>
  </div>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import Fuse from 'fuse.js'
import { genRoutes, fuseConfig } from './searchData'
import { filterRoutes } from '@/utils/route'
import { watchSwitchLang } from '@/i18n'

const isShow = ref(false)
const searchWords = ref('')
const searchInputRef = ref(null)
const searchResults = ref([])
const router = useRouter()
const searchData = genRoutes(filterRoutes(router.getRoutes()))
let fuse

function initFuse(data) {
  fuse = new Fuse(data, fuseConfig)
}
initFuse(searchData)

function toggleShowSearch() {
  isShow.value = !isShow.value
  searchInputRef.value.focus()
}

function onClose() {
  isShow.value = false
  searchResults.value = []
  searchWords.value = ''
}

watch(isShow, val => {
  if (val) {
    document.body.addEventListener('click', onClose)
  } else {
    document.body.removeEventListener('click', onClose)
  }
})

function onSearch(searchWords) {
  if (searchWords !== '') {
    searchResults.value = fuse.search(searchWords)
  } else {
    searchResults.value = []
  }
}

// 选中回调
function onSelectChange(val) {
  router.push(val.path)
  onClose()
}

watchSwitchLang(() => {
  initFuse(genRoutes(filterRoutes(router.getRoutes())))
})
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
