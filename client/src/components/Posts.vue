<template>
	<div class="w-full flex justify-center">
		<div v-if="loading">Loading...</div>
		<div v-else class="w-full max-w-[64rem] grid-container">
			<div v-for="item in data" :key="item._id">
				<ImageCard :imageUrl="item.imageUrl" :description="item.description" />
			</div>
		</div>
		<div v-if="error">{{ error }}</div>
	</div>
</template>

<script>
import ImageCard from "./ImageCard.vue";

export default {
	data() {
		return {
			loading: true,
			data: null,
			error: null,
		};
	},
	async mounted() {
		const apiUrl = "http://192.168.1.129:8001/posts/";
		try {
			const response = await fetch(apiUrl);
			if (!response.ok) {
				throw new Error("Network response was not ok");
			}
			const data = await response.json();
			this.data = data;
			this.loading = false;
		} catch (error) {
			console.error("Error fetching data:", error);
			this.error = "Error fetching data. Please try again later.";
			this.loading = false;
		}
	},
	components: { ImageCard },
};
</script>
