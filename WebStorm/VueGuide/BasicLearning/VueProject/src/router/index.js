import {createRouter, createWebHistory} from "vue-router";
import EmbellishTest from "@/router/EmbellishTest.js";

const router = createRouter({
    history: createWebHistory(),
    routes: [...EmbellishTest]
});

export default router;