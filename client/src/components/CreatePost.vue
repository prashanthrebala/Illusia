<template>
	<div class="w-full flex justify-center gap-3">
		<input
			type="text"
			placeholder="Enter a prompt..."
			class="max-w-[32rem] w-5/6 rounded-lg px-4 p-2 outline-0 h-12 md:h-14 border-2 border-neutral-600 bg-slate-100 text-neutral-800"
		/>
		<button
			class="bg-neutral-950 w-24 p-2 text-white rounded-lg flex justify-center items-center"
			@click="createPost"
		>
			Create!
		</button>
	</div>
	<div class="w-full h-24 flex justify-center items-center text-xs">
		Note that the image generated will automatically be visible to everyone who
		uses this website
	</div>
</template>

<script></script>
