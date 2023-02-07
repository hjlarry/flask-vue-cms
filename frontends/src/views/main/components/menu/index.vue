<template>
  <div class="py-2 h-[80vh] flex flex-col">
    <h2 class="text-lg text-zinc-900 font-bold mb-2 px-1">所有分类</h2>
    <ul class="overflow-y-scroll">
      <li
        v-for="(item, index) in data"
        :key="item.id"
        class="text-base text-zinc-900 px-1 py-1.5"
        ref="itemRef"
        @click="$emit('onItemClick', index)"
      >
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
interface Props {
  data: Array<{ id: string; name: string }>
}
defineProps<Props>()
</script>
