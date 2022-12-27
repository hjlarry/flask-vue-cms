<template>
  <el-dialog :title='$t("msg.theme.themeColorChange")' width='22%' :model-value='modelValue' center>
    <div class='center'>
      <el-color-picker
        v-model='mColor'
        :predefine='predefineColors'>
      </el-color-picker>
    </div>

    <template #footer>
      <el-button @click='closed'>{{ $t('msg.universal.cancel')}}</el-button>
      <el-button type='primary'>{{ $t('msg.universal.confirm')}}</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'

defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})
const emits = defineEmits(['update:modelValue'])
function closed() {
  emits('update:modelValue', false)
}

const predefineColors = [
  '#ff4500',
  '#ff8c00',
  '#ffd700',
  '#90ee90',
  '#00ced1',
  '#1e90ff',
  '#c71585',
  'rgba(255, 69, 0, 0.68)',
  'rgb(255, 120, 0)',
  'hsv(51, 100, 98)',
  'hsva(120, 40, 94, 0.5)',
  'hsl(181, 100%, 37%)',
  'hsla(209, 100%, 56%, 0.73)',
  '#c7158577'
]
const mColor = ref('#00ff00')
</script>

<style scoped>
.center {
  text-align: center;
}
</style>
