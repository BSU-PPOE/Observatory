# Observatory

**Hello Observatory World! i made a search bar!**

<style>
    .search-form {
        position: absolute;
        top: 80px;
        right: 10px;
    }
</style>

<form class="search-form" action="{{ url_for('search') }}" method="get">
    <!-- Search input -->
    <input type="text" name="query" placeholder="Enter your search query">
    <!-- Search button -->
    <button type="submit">Search</button>
</form>