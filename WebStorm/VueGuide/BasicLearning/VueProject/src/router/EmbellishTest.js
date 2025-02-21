const routes = [
    {
        path: "/list",
        component: () =>
            import("../components/ListEmbellish.vue")
    },
    {
        path: "/cdt",
        component: () =>
            import("../components/CdtEmbellish.vue")
    }
];

export default routes;