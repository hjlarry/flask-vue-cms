<template>
  <div
    class="relative h-screen text-center bg-white dark:bg-zinc-800 xl:bg-zinc-200"
  >
    <div class="pt-5 h-8">
      <m-svg-icon name="wei-bo" class="h-8 w-8 mx-auto"></m-svg-icon>
    </div>

    <div
      class="px-3 mt-4 dark:bg-zinc-800 xl:bg-white xl:dark:bg-zinc-900 xl:w-[388px] xl:mx-auto xl:mt-8 xl:py-4 xl:rounded-sm xl:shadow-lg"
    >
      <h3
        class="font-semibold text-base text-main dark:text-zinc-300 hidden xl:block"
      >
        账户登录
      </h3>

      <form>
        <input
          class="w-full text-base outline-0 border-b border-b-zinc-400 pb-1 px-1 focus:border-b-main dark:bg-zinc-800 dark:text-zinc-400 dark:focus:border-b-zinc-200 xl:dark:bg-zinc-900"
          placeholder="用户名"
          type="text"
          name="username"
          autocomplete="on"
        />

        <input
          class="w-full text-base outline-0 border-b border-b-zinc-400 pb-1 px-1 focus:border-b-main dark:bg-zinc-800 dark:text-zinc-400 dark:focus:border-b-zinc-200 xl:dark:bg-zinc-900"
          placeholder="密码"
          type="password"
          name="password"
          autocomplete="on"
        />

        <div class="pt-1 pb-3 text-right leading-[1px]">
          <a
            class="inline-block text-sm p-1 cursor-pointer text-zinc-400 hover:text-zinc-600"
            >去注册</a
          >
        </div>

        <m-button
          class="w-full dark:bg-zinc-900 xl:dark:bg-zinc-800"
          :isActiveAnim="false"
          >登录</m-button
        >
      </form>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
