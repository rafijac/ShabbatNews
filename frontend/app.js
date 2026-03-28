async function fetchAggregatedNews() {
    try {
        const res = await fetch('/api/aggregated-news');
        const data = await res.json();
        renderAggregatedNews(data);
    } catch (e) {
        document.getElementById('headlines').innerHTML = '<p style="color:red">Failed to load aggregated news.</p>';
    }
}

function renderAggregatedNews(data) {
    const container = document.getElementById('headlines');
    const lastUpdateDiv = document.getElementById('last-update');
    container.innerHTML = '';
    // Summary header
    if (data.summary_header) {
        const headerDiv = document.createElement('div');
        headerDiv.className = 'summary-header';
        headerDiv.innerHTML = `<h2>Summary</h2><p>${data.summary_header}</p>`;
        container.appendChild(headerDiv);
    }
    // Attributed news items
    if (Array.isArray(data.items)) {
        const ul = document.createElement('ul');
        ul.className = 'aggregated-list';
        data.items.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `<span class="headline-title">${item.summary}</span> <span class="headline-source">[<a href="${item.url}" target="_blank">${item.source}</a>]</span>`;
            ul.appendChild(li);
        });
        container.appendChild(ul);
    }
    lastUpdateDiv.innerHTML = '';
}

fetchAggregatedNews();
setInterval(fetchAggregatedNews, 60000);
