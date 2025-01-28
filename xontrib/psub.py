from xonsh.built_ins import XSH

def _psub_alias(args, stdin=None, stdout=None, stderr=None):
	import argparse
	import tempfile
	import subprocess
	import os
	import shutil
	from xonsh.events import events

	parser = argparse.ArgumentParser(prog='psub')
	parser.add_argument('-f', '--file', dest='fifo',
		action='store_false', default=False)
	parser.add_argument('-F', '--fifo', dest='fifo',
		action='store_true', default=False)
	parser.add_argument('-s', '--suffix', default='')
	args = parser.parse_args(args)

	if stdin is None:
		print('psub: no stdin', file=stderr)
		return 1
	if stdout is None:
		print('psub: no stdout', file=stderr)
		return 1

	tempdir = None
	@events.on_postcommand
	def cleanup(cmd, rtn, out, ts):
		if tempdir is not None:
			shutil.rmtree(tempdir)
		events.on_postcommand.remove(cleanup)
	tempdir = tempfile.mkdtemp(prefix='xonsh-psub.')
	filepath = os.path.join(tempdir, 'psub' + args.suffix)

	if args.fifo:
		os.mkfifo(filepath)
	else:
		os.mknod(filepath)
	proc = subprocess.Popen(['tee', filepath],
		stdin=stdin, stdout=subprocess.DEVNULL, stderr=stderr)
	if not args.fifo:
		proc.wait()

	stdout.write(filepath)
	return 0

XSH.aliases['psub'] = _psub_alias
