# Help on class StringIO in module io:

class _TextIOBase():
    def __init__(self):
        pass


class StringIO(_TextIOBase):
    """
    StringIO(initial_value='', newline='\n')

    Text I/O implementation using an in-memory buffer.

    The initial_value argument sets the value of object.  The newline
    argument is like the one of TextIOWrapper's constructor.

    Method resolution order:
        StringIO
        _TextIOBase
        _IOBase
        builtins.object

    Methods defined here:

    __getstate__(...)

    __init__(self, /, *args, **kwargs)
        Initialize self.  See help(type(self)) for accurate signature.

    __next__(self, /)
        Implement next(self).

    __setstate__(...)
    """

    def __init__(self):
        pass


    def close(self):
        """
        Close the IO object.

        Attempting any further operation after the object is closed
        will raise a ValueError.

        This method has no effect if the file is already closed.
        """
        pass


    def getvalue(self):
        """
        Retrieve the entire contents of the object.
        """
        pass


    def read(self, size=-1):
        """
        Read at most size characters, returned as a string.

        If the argument is negative or omitted, read until EOF
        is reached. Return an empty string at EOF.
        """
        pass


    def readable(self):
        """
        Returns True if the IO object can be read.
        """
        pass


    def readline(self, size=-1):
        """
        Read until newline or EOF.

        Returns an empty string if EOF is hit immediately.
        """
        pass


    def seek(self, pos, whence=0):
        """
        Change stream position.

        Seek to character offset pos relative to position indicated by whence:
            0  Start of stream (the default).  pos should be >= 0;
            1  Current position - pos must be 0;
            2  End of stream - pos must be 0.
        Returns the new absolute position.
        """
        pass


    def seekable(self):
        """
        Returns True if the IO object can be seeked.
        """
        pass


    def tell(self):
        """
        Tell the current file position.
        """
        pass


    def truncate(self, pos=None):
        """
        Truncate size to pos.

        The pos argument defaults to the current file position, as
        returned by tell().  The current file position is unchanged.
        Returns the new absolute position.
        """
        pass


    def writable(self):
        """
        Returns True if the IO object can be written.
        """
        pass


    def write(self, s):
        """
        Write string to file.

        Returns the number of characters written, which is always equal to
        the length of the string.
        """
        pass

    # ----------------------------------------------------------------------
    # Static methods defined here:

    # __new__(*args, **kwargs) from builtins.type
    # Create and return a new object.  See help(type) for accurate signature.

    # ----------------------------------------------------------------------
    # Data descriptors defined here:

    # closed

    # line_buffering

    # newlines
    # Line endings translated so far.

    # Only line endings translated during reading are considered.

    # Subclasses should override.

    # ----------------------------------------------------------------------
    # Methods inherited from _TextIOBase:

    # detach(...)
    # Separate the underlying buffer from the TextIOBase and return it.

    # After the underlying buffer has been detached, the TextIO is in an
    # unusable state.

    # ----------------------------------------------------------------------
    # Data descriptors inherited from _TextIOBase:

    # encoding
    # Encoding of the text stream.

    # Subclasses should override.

    # errors
    # The error setting of the decoder or encoder.

    # Subclasses should override.

    # ----------------------------------------------------------------------
    # Methods inherited from _IOBase:

    # __del__(...)

    # __enter__(...)

    # __exit__(...)

    # __iter__(self, /)
    # Implement iter(self).


    def fileno(self):
        """
        Returns underlying file descriptor if one exists.

        OSError is raised if the IO object does not use a file descriptor.
        """
        pass


    def flush(self):
        """
        Flush write buffers, if applicable.

        This is not implemented for read-only and non-blocking streams.
        """
        pass


    def isatty(self):
        """
        Return whether this is an 'interactive' stream.

        Return False if it can't be determined.
        """
        pass


    def readlines(self, hint=-1):
        """
        Return a list of lines from the stream.

        hint can be specified to control the number of lines read: no more
        lines will be read if the total size (in bytes/characters) of all
        lines so far exceeds hint.
        """
        pass


    def writelines(self, lines):
        """
        """
        pass

    # ----------------------------------------------------------------------
    # Data descriptors inherited from _IOBase:

    # __dict__