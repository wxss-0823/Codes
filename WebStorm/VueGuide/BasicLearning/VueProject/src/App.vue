<script setup>
import HelloVue from "./components/HelloVue.vue"
// import CdtEmbellish from "./components/CdtEmbellish.vue"
// import ListEmbellish from "./components/ListEmbellish.vue";

import { RouterView, RouterLink} from "vue-router";
import AjaxGet from "@/components/AjaxGet.vue";
</script>

<template>
  <header>
  </header>

  <main>
    <HelloVue msg="Hello Vue!" />
<!--    <div>-->
<!--      <CdtEmbellish />-->
<!--    </div>-->

<!--    <div>-->
<!--      <ListEmbellish />-->
<!--    </div>-->

    <div>
      <RouterLink to="/list">List Embellish</RouterLink>
      <br>
      <RouterLink to="/cdt">Conditional Embellish</RouterLink>
      <RouterView></RouterView>
    </div>

    <div>
      <AjaxGet></AjaxGet>
    </div>
  </main>
</template>

<style scoped>

</style>
