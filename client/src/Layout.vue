<script setup>
import illusiaBg from "./assets/illusia-bg.jpg";
import App from "./App.vue";

const backgroundStyle = {
	backgroundImage: `url(${illusiaBg})`,
};
</script>

<template>
	<div
		:style="backgroundStyle"
		class="w-full min-h-screen bg-no-repeat bg-cover bg-right fixed top-0 left-0 -z-10"
	/>
	<div class="w-full flex justify-center">
		<div class="w-full max-w-[100rem]">
			<App />
		</div>
	</div>
	<div class="w-full h-36 text-xs flex justify-end items-center p-20">
		<a
			href="https://www.freepik.com/free-photo/colorful-abstract-nebula-space-background_16263202.htm#query=red%20black%20background&position=9&from_view=search&track=ais"
			>Background image by rawpixel.com</a
		>
		&nbsp;on Freepik
	</div>
</template>
