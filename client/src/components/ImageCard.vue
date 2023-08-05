<script setup>
const { imageUrl, description } = defineProps({
	imageUrl: String,
	description: String,
});

const backgroundStyle = {
	backgroundImage: `url(${imageUrl})`,
};
</script>

<template>
	<div class="flex flex-col gap-1">
		<div class="w-96 h-96 bg-contain rounded-md" :style="backgroundStyle" />
		<div
			class="w-96 bg-rose-900 p-4 rounded-md flex items-center justify-center font-medium text-sm leading-6 text-neutral-100"
		>
			{{ description }}
		</div>
	</div>
</template>
