<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div>
    {{ msg }}
  </div>
</template>

<style scoped>

</style>
