const folders = [
    { name: 'Documents', icon: 'https://img.icons8.com/?size=100&id=40949&format=png&color=000000'},
    { name: 'Photos', icon: 'https://img.icons8.com/?size=100&id=RxzRPd8sH7Ru&format=png&color=000000' },
    { name: 'Music', icon: 'https://img.icons8.com/?size=100&id=kjouk7bBK9Nf&format=png&color=000000' },
    { name: 'Videos', icon: 'https://img.icons8.com/?size=100&id=t294OHA3a4ko&format=png&color=000000' },
    { name: 'Downloads', icon: 'https://img.icons8.com/?size=100&id=cnDcRP3O64a9&format=png&color=000000' },
];
function updateDateTime() {
    const now = new Date();
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    };
    const formattedDateTime = now.toLocaleString('en-US', options);
    document.getElementById('current-datetime').innerText = formattedDateTime;
}
function displayFolders() {
    const folderContainer = document.getElementById('folder-container');
    folders.forEach(folder => {
        const folderDiv = document.createElement('div');
        folderDiv.className = 'folder';
        folderDiv.innerHTML = `
            <img src="${folder.icon}" alt="${folder.name} icon">
            <div class="folder-name">${folder.name}</div>
        `;
        folderContainer.appendChild(folderDiv);
    });
}
displayFolders();
updateDateTime()
setInterval(updateDateTime, 1000);