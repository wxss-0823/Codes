<script setup>

</script>

<script>
export default {
  data() {
    return {
      isVisible: true
    };
  },
  methods: {
    toggleVisibility() {
      this.isVisible = !this.isVisible;
    }
  }

}
</script>

<template>
  <div>
    <p v-if="isVisible">This text is visible!</p>
    <button id="visibleButton" v-on:click="toggleVisibility">Toggle text visibility</button>
  </div>
</template>

<style scoped>

</style>