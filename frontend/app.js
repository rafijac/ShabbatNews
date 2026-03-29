function updateLastRefreshed() {
    const el = document.getElementById('last-refreshed');
    if (el) el.textContent = 'Last refreshed: ' + dayjs().format('HH:mm:ss');
}

function renderCol(listId, source) {
    const ul = document.getElementById(listId);
    if (!source || !source.headlines || source.headlines.length === 0) {
        ul.innerHTML = '<li class="error">No headlines available.</li>';
        return;
    }
    ul.innerHTML = source.headlines.map(h => {
        const ago = h.published ? dayjs(h.published).fromNow() : '';
        return `<li><span class="hl-title">${h.title}</span><span class="hl-ago">${ago}</span></li>`;
    }).join('');
}

async function fetchHeadlines() {
    try {
        const res = await fetch('/api/headlines');
        const data = await res.json();
        renderCol('list-toi', data.timesofisrael);
        updateLastRefreshed();
    } catch (e) {
        document.getElementById('list-toi').innerHTML = '<li class="error">Failed to load headlines.</li>';
    }
}

fetchHeadlines();
setInterval(fetchHeadlines, 60000);
