<script setup>

</script>

<script>
export default {
  data() {
    return {
      items: [
        { id: 1, name: 'Vue 3'},
        { id: 2, name: 'JavaScript'},
        { id: 3, name: 'HTML5'}
      ]
    };
  }
};
</script>

<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<style scoped>

</style>