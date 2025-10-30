```dataviewjs
dv.table(["Link", "Modified"],
	dv.pages()
		.where(p => p.file.mtime)
		.sort(p => p.file.mtime, 'desc')
		.map(p => [p.file.link, p.file.mtime.toFormat("yyyy-MM-dd HH:mm")])
        .limit(20)  
);
```


Relative path to Saga: 