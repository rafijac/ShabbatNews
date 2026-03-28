async function fetchHeadlines() {
    try {
        const res = await fetch('/api/headlines');
        const data = await res.json();
        renderCol('list-toi', data.timesofisrael);
        renderCol('list-ynet', data.ynet);
    } catch (e) {
        ['list-toi', 'list-ynet'].forEach(id => {
            document.getElementById(id).innerHTML = '<li class="error">Failed to load headlines.</li>';
        });
    }
}

function renderCol(listId, source) {
    const ul = document.getElementById(listId);
    if (!source || !source.headlines) { ul.innerHTML = '<li class="error">No data.</li>'; return; }
    ul.innerHTML = source.headlines.map(h => {
        const ago = h.published ? dayjs(h.published).fromNow() : '';
        return `<li><span class="hl-title">${h.title}</span><span class="hl-ago">${ago}</span></li>`;
    }).join('');
}

fetchHeadlines();
setInterval(fetchHeadlines, 60000);
