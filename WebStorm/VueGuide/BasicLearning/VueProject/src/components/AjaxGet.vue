<script setup>

</script>

<script>
import axios from "axios";

export default {
  data() {
    return {
      info: "Ajax Test!!"
    }
  },
  mounted() {
    axios
      .get('http://localhost:5173/cdt')
      .then(res => {this.info = res.config.method;})
      .catch((err) => {
        console.log(err);
      });
  }
}

</script>

<template>
  <div>
    {{ info }}
  </div>
</template>

<style scoped>

</style>