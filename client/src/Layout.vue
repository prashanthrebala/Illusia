<script setup>
import illusiaBg from "./assets/illusia-bg.jpg";

const backgroundStyle = {
	backgroundImage: `url(${illusiaBg})`,
};
</script>

<template>
	<div
		:style="backgroundStyle"
		class="w-full min-h-screen bg-no-repeat bg-cover bg-right absolute top-0 left-0 -z-10 bg-amber-300"
	/>
	<div class="w-full flex justify-center">
		<div class="w-full max-w-[100rem]"></div>
	</div>
</template>
