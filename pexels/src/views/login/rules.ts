import { defineRule } from 'vee-validate'

defineRule('required', (value) => {
  if (!value || !value.length) {
    return 'This field is required'
  }
  return true
})

defineRule('minLength', (value, [limit]) => {
  if (value.length < limit) {
    return `This field must be at least ${limit} characters`
  }
  return true
})

defineRule('maxLength', (value, [limit]) => {
  if (value.length > limit) {
    return `This field must less than ${limit} characters`
  }
  return true
})

defineRule('confirmed', (value, [target], ctx) => {
  if (value === ctx.form[target]) {
    return true
  }
  return 'Passwords must match'
})
