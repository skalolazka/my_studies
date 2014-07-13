#!/usr/bin/perl

use strict;
use warnings;

package MyQueueFromStacks;

sub new {
    my ($class, @values) = @_;
    my $self = {
        stack1 => [], # enqueue here
        stack2 => [], # dequeue from this
    };
    bless $self => $class;
    for (@values) {
        $self->enqueue($_);
    }
    return $self;
}

sub enqueue {
    my ($self, $val) = @_;
    push(@{$self->{stack1}}, $val);
    return $val;
}

sub dequeue {
    my $self = shift;
    my $result;
    if (!scalar(@{$self->{stack2}})) {
        while (scalar(@{$self->{stack1}})) {
            my $val = pop(@{$self->{stack1}});
            push(@{$self->{stack2}}, $val);
        }
    }
    return pop(@{$self->{stack2}});
}


package TestMyQueueFromStacks;

my $m = MyQueueFromStacks->new;

use Test::More tests => 14;

is($m->dequeue, undef, 'nothing to dequeue');
is($m->enqueue(2), 2, 'enqueued');
$m->enqueue(3);
$m->enqueue(4);
$m->enqueue(5);
is($m->dequeue, 2, 'one');
is($m->dequeue, 3, 'two');
is($m->dequeue, 4, 'three');
is($m->dequeue, 5, 'four');
is($m->dequeue, undef, 'none left');
$m->enqueue(3);
is($m->dequeue, 3, 'again');
$m = MyQueueFromStacks->new(1,2,3);
is($m->dequeue, 1, 'from full');
is($m->dequeue, 2, 'from full again');
$m->enqueue(4);
is($m->dequeue, 3, 'from full again and again');
$m->enqueue(5);
$m->enqueue(6);
$m->enqueue(7);
is($m->dequeue, 4, 'from full again and again');
is($m->dequeue, 5, 'from full again and again');
$m->enqueue(8);
is($m->dequeue, 6, 'from full again and again');

#done_testing();
