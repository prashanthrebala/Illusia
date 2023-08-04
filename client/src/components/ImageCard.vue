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
	<div class="flex flex-col gap-2">
		<div
			class="w-full max-w-[24rem] aspect-square bg-contain rounded-md"
			:style="backgroundStyle"
		/>
		<div
			class="w-full max-w-[24rem] bg-rose-900 p-4 rounded-md flex justify-center text-center font-medium text-sm leading-6 text-neutral-100"
		>
			{{ description }}
		</div>
	</div>
</template>
