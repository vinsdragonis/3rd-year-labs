#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 199309L
#include&lt;stdio.h&gt;
#include&lt;unistd.h&gt;

int main()
{
	#ifdef _POSIX_JOB_CONTROL
		printf(&quot;System supports job control\n&quot;);
	#else
		printf(&quot;System does not support job control \n&quot;);
	#endif
	
	#ifdef _POSIX_SAVED_IDS
		printf(&quot;System supports saved set-UID and saved set-GID\n&quot;);
	#else
		printf(&quot;System does not support saved set-UID and saved set-GID \n&quot;);
	#endif
	
	#ifdef _POSIX_CHOWN_RESTRICTED
		printf(&quot;chown_restricted option is %d\n”,
	_POSIX_CHOWN_RESTRICTED);
	#else
		printf(&quot;System does not support chown_restricted option \n&quot;);
	#endif
	
	#ifdef _POSIX_NO_TRUNC
		printf(&quot;Pathname trunc option is %d\n&quot;,_POSIX_NO_TRUNC);
	#else
		printf(&quot;System does not support system-wide pathname trunc option \n&quot;);
	#endif
	
	#ifdef _POSIX_VDISABLE
		printf(&quot;Disable character for terminal files is %d\n&quot;,
	_POSIX_VDISABLE);
	#else
		printf(&quot; System does not support _POSIX_VDISABLE \n&quot;);
	#endif
	
	return 0;
}
