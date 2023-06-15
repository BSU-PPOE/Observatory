# Observatory

**Hello Observatory World! i made a search bar!**

Search Our Database:

<form method="POST" action="{{ url_for('search') }}">
    <input type="text" name="search_query" placeholder="Search">
    <button type="submit">Search</button>
</form>