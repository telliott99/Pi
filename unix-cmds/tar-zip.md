#### tar and zip

Collections of files can be bundled together in archives.  The original archives were written to magnetic tape and are called tape archives and the tool is called **tar**. 

Also, files often have a lot of empty space which can be removed by compression.

Standard usage:

```
tar -zcvf archive.tar.gz <source-directory>
```

The ``c`` flag is for create.  To reverse the archival process and recover the original directory, do ``x`` (extract):

```
tar -zcvf archive.tar.gz <source-directory>
```

The other flags:

- ``z`` compress the result with ``gzip`` 
- ``v`` (verbose)
- ``f`` (file)

 ``f`` means "read the archive from or write the archive to the specified file."
 
 Use ``tar``.  No reason to run ``gzip``.  Also, gzipped archives are automatically recognized.
 
 For a comparison see this [answer](https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip).
 
> For reasonably large archives there are important differences though. A zip archive is a catalog of compressed files. With a gzipped tar, it is a compressed catalog, of files. Thus a zip archive is a randomly accessible list of concatenated compressed items, and a .tar.gz is an archive that must be fully expanded before the catalog is accessible.

- zip:  you don't get compression across files.
- .tar.gz:  you must decompress the whole archive.
