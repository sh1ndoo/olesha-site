import Home from "@/pages/Home.vue";
import {createRouter, createWebHistory} from "vue-router";
import Games from "@/pages/Games.vue";
import Rules from "@/pages/Rules.vue";
import Commands from "@/pages/Commands.vue";
import Commercial from "@/pages/Commercial.vue";
import Art from "@/pages/Art.vue";
import List from "@/pages/List.vue";
import ArticleView from "@/pages/ArticleView.vue";
import ArticleList from "@/pages/ArticleList.vue";
import Scrandle from "@/pages/Scrandle.vue";
import ScrandleMenu from "@/pages/ScrandleMenu.vue";
import ScrandleVote from "@/pages/ScrandleVote.vue";
import Profile from "@/pages/Profile.vue";
import Streamle from "@/pages/Streamle.vue";
const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/games',
        component: Games
    },
    {
        path: '/rules',
        component: Rules
    },
    {
        path: '/commands',
        component: Commands
    },
    {
        path: '/commercial',
        component: Commercial
    },
    {
        path: '/art',
        component: Art
    },
    {
        path: '/list',
        component: List
    },
    {
        path: '/articles',
        component: ArticleList
    },
    {
        path: '/articles/:id',
        component: ArticleView
    },
    {
        path: '/scrandle',
        component: Scrandle
    },
    {
        path: '/profile',
        component: Profile
    },
    {
        path: '/streamle',
        component: Streamle
    }
]

const router = createRouter(
    {
        routes,
        history: createWebHistory()
    }
)

export default router